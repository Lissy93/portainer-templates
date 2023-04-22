<script lang="ts">
  import type { Template } from '$src/Types';
  export let templates: Template[];
  import { lazyLoad } from '$lib/lazy-load';

  const slugify = (title: string) => {
    return `/${title.toLowerCase().replace(/[^a-zA-Z ]/g, "").replaceAll(' ', '-')}`;
  }
</script>

<section class="templates">
  {#each templates as template (template.title)}
    <a class="template-card" href={slugify(template.title)}>
      <h3>{template.title}</h3>
      <div class="template-summary">
        <div class="left">
          <img class="loading" use:lazyLoad={template.logo} alt={template.title} />
        </div>
        <div class="txt">
          <p class="description" title={template.description}>{template.description}</p>
        </div>
      </div>
    </a>
  {/each}
</section>

<style lang="scss">
section.templates {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1rem;
  margin: 1rem auto;
  padding: 0 1rem;
  max-width: var(--max-width);
  .template-card {
    padding: 1rem;
    border-radius: 6px;
    background: var(--card);
    display: flex;
    flex-direction: column;
    gap: 1rem;
    transition:all 0.3s ease-in-out;
    max-width: 28rem;
    text-decoration: none;
    color: var(--foreground);
    &:hover {
      box-shadow: var(--shadow);
    }
    .template-summary {
      display: flex;
      gap: 1rem;
      align-items: start;
    }
    p, h3 {
      margin: 0;
    }
    img {
      width: 64px;
      max-height: 64px;
      border-radius: 6px;
      &.loading {
        padding: 0.2rem;
        background: var(--card-2);
        border-radius: 6px;
        height: 64px;
      }
    }
    .description {
      font-style: italic;
      font-weight: 200;
      overflow: hidden;
      word-break: break-word;
      text-overflow: ellipsis;
      display: -webkit-box;
      -webkit-box-orient: vertical;
      -webkit-line-clamp: 5;
      line-clamp: 5; 
    }
  }
}
</style>