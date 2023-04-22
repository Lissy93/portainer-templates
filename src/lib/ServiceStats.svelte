<script lang="ts">
  import type { TemplateOrService } from '$src/Types';

  export let template: TemplateOrService;
</script>


<div class="stats">
  {#if template.type}
    <span class="lbl">Type</span>
    {#if template.type === 1}
      <span class="val">Container</span>
    {:else if template.type === 2}
      <span class="val">Swarm</span>
    {:else if template.type === 3}
      <span class="val">Kubernetes</span>
    {:else}
      <span class="val">Unknown</span>
    {/if}
  {/if}
  {#if template.platform}
    <span class="lbl">Platform</span>
    <code class="val">{template.platform}</code>
  {/if}
  {#if template.image}
    <span class="lbl">Image</span>
    <code class="val">{template.image}</code>
  {/if}
  {#if template.command}
    <span class="lbl">Command</span>
    <code class="val">{template.command}</code>
  {/if}
  {#if typeof template.interactive === 'boolean'}
    <span class="lbl">Interactive</span>
    <code class="val">{template.interactive ? 'Yes' : 'No'}</code>
  {/if}
  {#if template.ports}
    <span class="lbl">Ports</span>
    <p class="val">
      {#each template.ports as port}<code>{port}</code>{/each}
    </p>
  {/if}
  {#if template.volumes}
    <span class="lbl">Volumes</span>
    <p class="val">
      {#each template.volumes as volume}
      <code>
        {volume.container || volume}{volume?.bind? ' : ' + volume.bind : ''}
      </code>{/each}
    </p>
  {/if}
  {#if template.restart_policy}
    <span class="lbl">Restart Policy</span>
    <code class="val">{template.restart_policy}</code>
  {/if}
  {#if template.repository}
    <span class="lbl">Sourced</span>
    <a class="val" href={template.repository.url}>Repo</a>
  {/if}
  {#if template.entrypoint}
    <span class="lbl">Entrypoint</span>
    <code class="val">{template.entrypoint}</code>
  {/if}
  {#if template.build}
    <span class="lbl">Build</span>
    <code class="val">{template.build}</code>
  {/if}
  {#if template.env}
    <span class="lbl">Env Vars</span>
    <p class="val">
      {#each template.env as env}<code>{env.name}={env.set || env.value || env.default || '\'\''}</code>{/each}
    </p>
  {/if}
</div>

<style lang="scss">
  .stats {
    min-width: 15rem;
    padding: 0.5rem;
    gap: 0.5rem;
    border-radius: 6px;
    display: grid;
    grid-template-columns: 1fr auto;
    place-items: baseline;
    background: var(--card-2);

    .lbl {
      font-weight: 400;
      font-style: normal;
    }

    .val {
      max-width: 10rem;
      overflow: hidden;
      white-space:nowrap;
      text-overflow: ellipsis;
    }

    span {
      font-style: italic;
    }
    p {
      margin: 0;
      display: flex;
      flex-direction: column;
    }

    a {
      color: var(--accent);
    }
  }
  
</style>
