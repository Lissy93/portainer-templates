<script lang="ts">
  import Highlight from "svelte-highlight";
  import yamlHighlight from "svelte-highlight/languages/yaml";
  import shellHighlight from "svelte-highlight/languages/shell";
  import codeHighlighting from "svelte-highlight/styles/dracula";

  import {
      generateDockerRunCommand,
      generateDockerRunCommands,
      convertToDockerCompose,
      convertPortainerStackToDockerCompose,
    } from '$src/utils/template-to-docker-parser';
  import { templatesUrl, gitHubRepo } from '$src/constants';
  import type { Template, Volume, Service, DockerCompose } from '$src/Types';

  export let portainerTemplate: Template | null = null;
  export let portainerServices: Service[] | null = null;

  const copyToClipboard = (content: string) => {
    navigator.clipboard.writeText(content);
  };

  const dockerRunCommand = portainerTemplate?.image ?
    generateDockerRunCommand(portainerTemplate) : null;
  const dockerRunCommands = portainerServices && !dockerRunCommand ?
    generateDockerRunCommands(portainerServices) : null;
  const dockerComposeFile = portainerTemplate?.image ?
    convertToDockerCompose(portainerTemplate) :
    (portainerServices ? convertPortainerStackToDockerCompose(portainerServices) : null);
</script>


<svelte:head>
  {@html codeHighlighting}
</svelte:head>

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
  <pre class="template-url">{templatesUrl}</pre>
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
      <Highlight language={shellHighlight} code={dockerRunCommand} />
    </div>
  {/if}

  {#if dockerRunCommands && dockerRunCommands.length > 0}
    <hr />
    <h3>Via Docker Run</h3>
    {#each dockerRunCommands as command, index}
      <h4>Service #{index + 1} - {portainerServices[index].name}</h4>
      <div class="docker-run-command">
        <button class="docker-command-copy" on:click={() => copyToClipboard(command)}>Copy</button>
        <Highlight language={shellHighlight} code={command} />
      </div>
    {/each}
  {/if}
  
  {#if dockerComposeFile}
    <hr />
    <h3>Via Docker Compose</h3>
    <p class="instructions">
      Save this file as <code>docker-compose.yml</code> and run <code>docker-compose up -d</code>
      <br>
      Use this only as a guide.
    </p>
    <div class="docker-compose-file">
      <button class="docker-command-copy" on:click={() => copyToClipboard(JSON.stringify(dockerComposeFile, null, 2))}>Copy</button>
      <Highlight language={yamlHighlight} code={dockerComposeFile} />
    </div>
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
      &.template-url {
        white-space: normal;
      }
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
    .docker-run-command, .docker-compose-file {
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
    .instructions {
      margin-bottom: 0.5rem;
      font-size: 1rem;
      code {
        border-radius: 6px;
        padding: 0 0.25rem;
        background: var(--card-2);
      }
    }
    :global(.hljs) {
      background: var(--card-2);
      font-size: 1.1rem;
      padding: 0;
    }
  }
</style>