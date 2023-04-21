<script lang="ts">
  import type { TemplateOrService } from '$src/Types';

  export let template: TemplateOrService;
</script>


<div class="stats">
  {#if template.type}
    <div class="row">
      <span class="lbl">Type</span>
      {#if template.type === 1}
        <span>Container</span>
      {:else if template.type === 2}
        <span>Swarm</span>
      {:else if template.type === 3}
        <span>Kubernetes</span>
      {:else}
        <span>Unknown</span>
      {/if}
    </div>
  {/if}
  {#if template.platform}
    <div class="row">
      <span class="lbl">Platform</span>
      <code>{template.platform}</code>
    </div>
  {/if}
  {#if template.image}
    <div class="row">
      <span class="lbl">Image</span>
      <code>{template.image}</code>
    </div>
  {/if}
  {#if template.command}
    <div class="row">
      <span class="lbl">Command</span>
      <code>{template.command}</code>
    </div>
  {/if}
  {#if typeof template.interactive === 'boolean'}
    <div class="row">
      <span class="lbl">Interactive</span>
      <code>{template.interactive ? 'Yes' : 'No'}</code>
    </div>
  {/if}
  {#if template.ports}
    <div class="row">
      <span class="lbl">Ports</span>
      <p>
        {#each template.ports as port}<code>{port}</code>{/each}
      </p>
    </div>
  {/if}
  {#if template.volumes}
    <div class="row">
      <span class="lbl">Volumes</span>
      <p>
        {#each template.volumes as volume}<code>{volume.container || volume}</code>{/each}
      </p>
    </div>
  {/if}
  {#if template.restart_policy}
    <div class="row">
      <span class="lbl">Restart Policy</span>
      <code>{template.restart_policy}</code>
    </div>
  {/if}
  {#if template.repository}
  <div class="row">
    <span class="lbl">Sourced</span>
    <a href={template.repository.url}>Repo</a>
  </div>
  {/if}
  {#if template.entrypoint}
  <div class="row">
    <span class="lbl">Entrypoint</span>
    <code>{template.entrypoint}</code>
  </div>
  {/if}
  {#if template.build}
  <div class="row">
    <span class="lbl">Build</span>
    <code>{template.build}</code>
  </div>
  {/if}
  {#if template.env}
  <div class="row">
    <span class="lbl">Env Vars</span>
    <p>
      {#each template.env as env}<code>{env.name}={env.set || env.value || env.default}</code>{/each}
    </p>
  </div>
  {/if}
</div>

<style lang="scss">
  .stats {
    min-width: 15rem;
    border: 2px solid var(--background);
    border-radius: 6px;
    .row {
      display: flex;
      justify-content: space-between;
      flex-wrap: wrap;
      padding: 0.5rem;
      gap: 0.5rem;
      &:not(:last-child) {
        border-bottom: 2px dotted var(--background);
      }
      span {
        font-style: italic;
      }
      p {
        margin: 0;
        display: flex;
        flex-direction: column;
      }
      .lbl {
        font-weight: 400;
        font-style: normal;
        min-width: 5rem;
      }
      a {
        color: var(--accent);
      }
    }
  }
</style>
