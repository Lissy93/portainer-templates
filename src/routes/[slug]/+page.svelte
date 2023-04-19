<script lang="ts">
  import { page } from '$app/stores';
  import TemplateNotFound from '$lib/TemplateNotFound.svelte';
  import type { Template } from '$src/Types';

  const templates = $page.data.templates as Template[];
  const templateSlug = $page.params.slug as string;
  
  const template = templates.find((temp: Template) =>
    temp.title.toLowerCase().replace(/[^a-zA-Z ]/g, "").replaceAll(' ', '-') === templateSlug
  );

  console.log(template);
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
    <h1><img src={template.logo} alt={template.title} />{template.title}</h1>
    {#if template.categories}
      <p class="tags">
        {#each (template.categories) as tag}
          <span>{tag}</span>
        {/each}
      </p>
    {/if}
    <div class="content">
      <p class="description">{template.description}</p>
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
            {#each template.volumes as volume}<code>{volume.container}</code>{/each}
          </p>
        </div>
      {/if}
      </div>
    </div>
  </section>
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
    .stats {
      min-width: 15rem;
      border: 2px solid var(--background);
      border-radius: 6px;
      .row {
        display: flex;
        justify-content: space-between;
        align-items: center;
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
      }
    }
  }
</style>