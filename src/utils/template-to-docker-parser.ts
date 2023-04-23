
import yaml from 'js-yaml';
import type { Template, Volume, Service, DockerCompose } from '$src/Types';

export const generateDockerRunCommand = (template: Template) => {
  let command = `docker run -d \\ \n`;
  if (template.ports) {
    template.ports.forEach((port) => {
      command += `  -p ${port} \\\n`;
    });
  }
  if (template.env) {
    template.env.forEach((env) => {
      command += `  -e ${env.name}=\${${env.name}} \\\n`;
    });
  }
  if (template.volumes) {
    template.volumes.forEach((volume: Volume) => {
      const readOnly = volume.readonly ? ":ro" : "";
      command += `  -v ${volume.bind}:${volume.container}${readOnly} \\\n`;
    });
  }
  if (template.restart_policy) {
    command += `  --restart=${template.restart_policy} \\\n`;
  }
  command += `  ${template.image}`;
  return command;
};

export const generateDockerRunCommands = (stack: Service[]) => {
  const commands = stack.filter((s) => s.image).map((service) => {
    let cmd = `docker run --name ${service.name} -d \\\n`;
    if (service.command) {
      cmd += ` ${service.command} \\\n`;
    }
    if (service.env) {
      service.env.forEach((envVar) => {
        cmd += ` -e "${envVar.value}" \\\n`;
      });
    }
    if (service.ports) {
      service.ports.forEach((port) => {
        cmd += ` -p ${port} \\\n`;
      });
    }
    if (service.volumes) {
      service.volumes.forEach((volume) => {
        cmd += ` -v ${volume.bind}:${volume.container} \\\n`;
      });
    }
    if (service.restart_policy) {
      cmd += ` --restart=${service.restart_policy} \\\n`;
    }
    cmd += ` ${service.image}`;
    return cmd;
  });
  return commands;
}

export const convertToDockerCompose = (template: Template) => {
  const serviceName = template.title.toLowerCase().replace(/[^a-z0-9]+/g, "-");
  const dockerCompose: DockerCompose = {
    version: "3.8",
    services: { [serviceName]: { image: template.image } },
  };
  if (template.ports && template.ports.length > 0) {
    dockerCompose.services[serviceName].ports = template.ports.map((port) => port.replace('/', ':'));
  }
  if (template.env && template.env.length > 0) {
    dockerCompose.services[serviceName].environment = template.env.reduce((envVars, envVar) => {
      envVars[envVar.name] = envVar.set || "";
      return envVars;
    }, {});
  }
  if (template.volumes && template.volumes.length > 0) {
    dockerCompose.services[serviceName].volumes = template.volumes.map(
      (volume) => `${volume.bind || ""}:${volume.container}`
    );
  }

  return yaml.dump(dockerCompose);
};

export const convertPortainerStackToDockerCompose = (stack: Service[]) => {
  const composeStack = stack.map(({ dockerStats, ...s }) => s);
  return yaml.dump(composeStack);
};

