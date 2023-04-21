<script lang="ts">
  import yaml from 'js-yaml';

  import { page } from '$app/stores';
  import TemplateNotFound from '$lib/TemplateNotFound.svelte';
  import type { Template, Service } from '$src/Types';

  import ServiceStats from '$lib/ServiceStats.svelte';
  const templates = $page.data.templates as Template[];
  const templateSlug = $page.params.slug as string;
  
  const template = templates.find((temp: Template) =>
    temp.title.toLowerCase().replace(/[^a-zA-Z ]/g, "").replaceAll(' ', '-') === templateSlug
  );

  console.log(template);


type Service = {
  name: string;
  image: string;
  entrypoint: string;
  command: string;
  ports: string[];
  build: string;
  interactive: boolean;
  volumes: { bind: string; container: string }[];
  restart_policy: string;
  environment: { name: string; value: string }[];
};

const getServices = async (): Promise<Service[]> => {
  try {
    if (template?.repository) {
      const { url: repoUrl, stackfile } = template.repository;
      const path = `${repoUrl.replace(
        'github.com',
        'raw.githubusercontent.com'
      )}/HEAD/${stackfile}`;
      const response = await fetch(path);
      const data = await response.text();
      const parsedData = yaml.load(data);
      const someServices: Service[] = [];
      if (!parsedData.services) return [];

      console.log(parsedData);
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
          env: Object.keys(serviceData.environment || {}).map((envName) => ({
            name: envName,
            value: serviceData.environment[envName],
          })),
        });
      });
      console.log(someServices);
      return someServices;
    } else {
      return [];
    }
  } catch (error) {
    console.error('Error fetching or parsing YAML:', error);
    return [];
  }
};

const services: Service[] = getServices();

</script>

<header>
  <a class="title" href="/">
    <img src="https://i.ibb.co/hMymwH0/portainer-templates-small.png" />
    <h2>Portainer Templates</h2>
  </a>
  <nav>
    <a href="/">Home</a>
    <a href="https://github.com/lissy93/portainer-templates">View on GitHub</a>
  </nav>
</header>

{#if template}
  <section class="summary-section">
    <h1>
      {#if template.logo} <img src={template.logo} /> {/if}
      {template.title}
    </h1>
    {#if template.categories || template.category }
      <p class="tags">
        {#each (template.categories || template.category || []) as tag}
          <span>{tag}</span>
        {/each}
      </p>
    {/if}
    <div class="content">
      <p class="description">{template.description}</p>
      <ServiceStats template={template} />
    </div>
  </section>

  {#await services then returnedServices}
  {#if returnedServices && returnedServices.length > 0}
    <section class="service-section">
      <h2>Services</h2>
      <div class="service-list">
        {#each returnedServices as service}
          <div>
            <h3>{service.name}</h3>
            <ServiceStats template={service} />
          </div>
        {/each}
      </div>
    </section>
  {/if}
  {/await}
{:else}
  <TemplateNotFound />
{/if}

<style lang="scss">
  header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: var(--card);
    padding: 0.25rem 1rem;
    a.title {
      display: flex;
      justify-content: center;
      gap: 1rem;
      color: var(--foreground);
      text-decoration: none;
      h2 {
        margin: 0;
        font-size: 1.5rem;
        font-weight: 600;
      }
      img {
        width: 40px;
        transition: all 0.3s ease-in-out;
      }
      &:hover {
        img { transform: rotate(-5deg) scale(1.1); }
      }
    }

    nav {
      display: flex;
      gap: 1rem;
      a {
        color: var(--foreground);
        text-decoration: none;
        padding: 0.25rem 0.5rem;
        border-radius: 6px;
        transition: all 250ms ease-in-out;
        &:hover {
          background: var(--gradient);
          transform: scale(1.05);
        }
      }
    }
  }
  .summary-section {
    background: var(--card);
    border-radius: 6px;
    padding: 1rem;
    margin: 1rem;
    display: flex;
    flex-direction: column;
    h1 {
      font-size: 4rem;
      margin: 0;
      display: flex;
      align-items: center;
      gap: 1rem;
    }
    img {
      border-radius: 6px;
      width: 64px;
      max-height: 64px;
    }
    .tags {
      display: flex;
      margin: 0;
      span {
        &:before {
          content: '#';
          opacity: 0.5;
        }
        &:not(:last-child)::after {
          content: ',';
          margin-right: 0.5rem;
        }
      }
    }
  }

  .content {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    justify-content: space-between;
    p.description {
      max-width: 60%;
    }
  }

  .service-section {
    background: var(--card);
    border-radius: 6px;
    margin: 1rem;
    padding: 1rem;
    h2 {
      margin: 0;
      font-size: 2rem;
    }
    .service-list {
      display: flex;
      gap: 1rem;
      // justify-content: space-between;
      flex-wrap: wrap;
      h3 {
        margin: 0.5rem 0;
        font-weight: 400;
      }
    }
  }
</style>
