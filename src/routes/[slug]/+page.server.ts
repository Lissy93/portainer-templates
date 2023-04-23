import yaml from 'js-yaml';

import { get } from 'svelte/store';
import { templatesUrl } from '$src/constants';
import { templates } from '$src/store';

/* Based on the current page name, find the corresponding template */
const findTemplate = (templates: any, slug: string) => {
  return templates.find((temp: Template) =>
    temp.title.toLowerCase().replace(/[^a-zA-Z ]/g, "").replaceAll(' ', '-') === slug
  );
};

/* With a given image name, fetch stats from DockerHub registry */
const getDockerHubStats = async (image: string): Promise<DockerHubResponse | null> => {
  if (!image) return null;
  const [imageName, tag] = image.split(':');
  const [namespace, repo] = imageName.includes('/') ? imageName.split('/') : ['library', imageName];
  const apiEndpoint = `https://hub.docker.com/v2/repositories/${namespace}/${repo}/`;

  return await fetch(apiEndpoint)
    .then((res) => res.json())
    .then((data) => {
      return data;
    })
    .catch((err) => {
      return null;
    });
}
const getServices = async (template): Promise<Service[]> => {
  try {
    if (template?.repository) {
      const { url: repoUrl, stackfile } = template.repository;
      const path = `${repoUrl.replace('github.com', 'raw.githubusercontent.com')}/HEAD/${stackfile}`;
      const response = await fetch(path);
      const data = await response.text();
      const parsedData = yaml.load(data);
      const someServices: Service[] = [];
      if (!parsedData.services) return [];

      Object.keys(parsedData.services).forEach((service) => {
        const serviceData = parsedData.services[service];
        someServices.push({
          name: service,
          image: serviceData.image,
          entrypoint: serviceData.entrypoint,
          command: serviceData.command,
          ports: serviceData.ports,
          build: serviceData.build,
          interactive: serviceData.interactive,
          volumes: serviceData.volumes?.map((vol) => ({
            bind: vol.split(':')[0],
            container: vol.split(':')[1],
          })),
          restart_policy: serviceData.restart,
          env: Object.keys(serviceData.environment || {}).map((envName) => {
            if (typeof envName === 'string') {
              const nowItsArray = serviceData.environment[envName].split('=') || [];
              return { name: nowItsArray[0] || '',  value: nowItsArray[1] || '' }
            }
            return { name: envName, value: serviceData.environment[envName] }
          }),
        });
      });
      return someServices;
    } else {
      return [];
    }
  } catch (error) {
    console.error('Error fetching or parsing YAML:', error);
    return [];
  }
};

/* Format results for returning to component */
const returnResults = async (templates, templateSlug) => {
  // Find template, based on slug
  let template = findTemplate(get(templates), templateSlug);

  // Fetch service info from associated stackfile, if it exists
  let services = template?.repository ? await getServices(template) : [];

  // If only 1 service, merge it with the template
  if (services.length === 1) {
    template = {...template, ...services[0]};
  } else if (services.length > 1) {
    // If made up from multiple services, fetch Docker info for each image
    services = await Promise.all(
      services.map(async (service) => {
        const dockerStats = await getDockerHubStats(service.image);
        return { ...service, dockerStats };
      })
    );
  }
  // If image specified, fetch Docker image info from DockerHub
  const dockerStats = template?.image ? await getDockerHubStats(template.image) : null;
  return { template, dockerStats, services }
};

export const load = async ({ params }) => {
  const templateSlug = params.slug as string;
  if (get(templates) && get(templates).length > 0) {
    return returnResults(templates, templateSlug);
  } else {
    const data = await fetch(templatesUrl).then((res) => res.json());
    templates.set(data.templates);
    return returnResults(templates, templateSlug);
  }
};
