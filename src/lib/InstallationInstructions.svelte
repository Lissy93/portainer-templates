<script lang="ts">

  import { templatesUrl, gitHubRepo } from '$src/constants';
  import type { Template, Volume, Service } from '$src/Types';

  export let portainerTemplate: Template | null = null;
  export let portainerServices: Service[] | null = null;

  const copyToClipboard = (content: string) => {
    navigator.clipboard.writeText(content);
  };

  const generateDockerRunCommand = (template: Template) => {
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

  const generateDockerRunCommands = (stack: Service[]) => {
    const commands = stack.map((service) => {
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

  const dockerRunCommand = portainerTemplate?.image ? generateDockerRunCommand(portainerTemplate) : null;
  const dockerRunCommands = portainerServices && !dockerRunCommand ? generateDockerRunCommands(portainerServices) : null;

</script>

<section>
  <h2>Installation</h2>

  <h3>Via Portainer</h3>
  <ol>
    <li>
      Ensure both
      <a href="https://docs.docker.com/engine/install/">Docker</a> and
      <a href="https://www.portainer.io/installation/">Portainer</a> are installed, and up-to-date
    </li>
    <li>Log into your Portainer web UI
    <li>Under Settings → App Templates, paste the below URL</li>
    <li>Head to Home → App Templates, and the list of apps will show up</li>
    <li>Select the app you wish to deploy, fill in any config options, and hit Deploy</li>
  </ol>

  <h4>Template Import URL</h4>
  <pre>{templatesUrl}</pre>
  <button on:click={() => copyToClipboard(templatesUrl)}>Copy</button>

  <details>
    <summary>Show Me</summary>
    <img class="demo" src="https://i.ibb.co/XxGRjrs/portainer-templates-installation.gif" alt="demo" />
  </details>

  {#if dockerRunCommand}
    <hr />
    <h3>Via Docker Run</h3>
    <div class="docker-run-command">
      <button class="docker-command-copy" on:click={() => copyToClipboard(dockerRunCommand)}>Copy</button>
      <pre>{dockerRunCommand}</pre>
    </div>
  {/if}

  {#if dockerRunCommands}
    <hr />
    <h3>Via Docker Run</h3>

    {#each dockerRunCommands as command, index}
      <h4>Service #{index + 1} - {portainerServices[index].name}</h4>
      <div class="docker-run-command">
        <button class="docker-command-copy" on:click={() => copyToClipboard(command)}>Copy</button>
        <pre>{command}</pre>
      </div>
    {/each}

  {/if}

  <hr />
  <h3>Alternative Methods</h3>
  <p>For more installation options, see the <a href={gitHubRepo}>Documentation</a> in the GitHub repo</p>

</section>

<style lang="scss">
  section {
    background: var(--card);
    padding: 1rem;
    border-radius: 6px;
    margin: 1rem auto;
    max-width: 1000px;
    transition: all 0.2s ease-in-out;
    h2 {
      margin: 0;
      font-size: 2rem;
    }
    h3 {
      font-size: 1.5rem;
      margin: 0.5rem 0;
    }
    h4 {
      margin: 0.5rem 0;
    }
    p {
      margin: 0;
    }
    ol {
      margin: 0.5rem;
      padding: 0;
      list-style: none;
      li {
        counter-increment: item;
      }
      li:before {
        content: counter(item);
        color: var(--accent);
        margin-right: 0.5rem;
        font-weight: 600;
        width: 1ch;
        text-align: center;
        display: inline-block;
      }
    }
    hr {
      opacity: 0.5;
      margin: 1.5rem auto;
      height: 2px;
      border: none;
      background: var(--accent);
    }
    pre {
      background: var(--card-2);
      padding: 0.25rem 0.5rem;
      font-size: 1.1rem;
      width: fit-content;
      margin: 0.5rem 0;
      display: inline;
      border-radius: 6px;
    }
    button {
      background: var(--background);
      padding: 0.25rem 0.5rem;
      border-radius: 6px;
      border: none;
      color: var(--foreground);
      font-family: Kanit;
      font-size: 1.1rem;
      cursor: pointer;
      transition: all 0.2s ease-in-out;
      &:hover {
        background: var(--gradient);
        transform: scale(1.1) rotate(-1deg);
      }
    }
    a {
      color: var(--accent);
    }
    details {
      summary {
        cursor: pointer;
        font-weight: bold;
        &:hover {
          color: var(--accent);
        }
      }
    }
    .demo {
      display: block;
      margin: 0.5rem auto;
      border-radius: 6px;
      max-width: 50rem;
    }
    .docker-run-command {
      background: var(--card-2);
      position: relative;
      padding: 0.5rem;
      pre {
        font-size: 1rem;
      }
      .docker-command-copy {
        position: absolute;
        right: 0.5rem;
        top: 0.5rem;
      }
    }
  }
</style>