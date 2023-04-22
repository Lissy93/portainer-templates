<script lang="ts">
import { slide } from 'svelte/transition';
import snarkdown from 'snarkdown';
export let content: string;
export let multiContent: { name: string, content: string, description: string, visible: false }[];

let showDocs = false;

const toggleDocs = () => {
  showDocs = !showDocs;
};

</script>

<section class="docker-docs">
  <h2>Container Documentation</h2>
  {#if content}
    <button on:click={toggleDocs}>{ showDocs ? 'Hide' : 'Expand' } Content</button>
    {#if showDocs}
      <p transition:slide>{@html snarkdown(content)}</p>
    {/if}

  {:else if multiContent && multiContent.length > 0}
    {#each multiContent as { name, description, content, visible }}
      <h3>{name} Documentation</h3>
      <p class="desc">{description || ''}</p>
      <button on:click={() => visible = !visible}>{ visible ? 'Hide' : 'Expand' } {name}</button>
      {#if visible}
        <p transition:slide>{@html snarkdown(content)}</p>
      {/if}
    {/each}
  {/if}
</section>

<style lang="scss">
  .docker-docs {
    background: var(--card);
    padding: 1rem;
    border-radius: 6px;
    margin: 1rem auto;
    max-width: 1000px;
    transition: all 0.2s ease-in-out;
    button {
      background: var(--background);
      padding: 0.25rem 0.5rem;
      border-radius: 6px;
      border: none;
      color: var(--foreground);
      font-family: Kanit;
      font-size: 1.2rem;
      cursor: pointer;
      transition: all 0.2s ease-in-out;
      &:hover {
        background: var(--gradient);
        transform: scale(1.1) rotate(-1deg);
      }
    }
    h2 {
      font-size: 2rem;
      margin: 0;
    }
    h3 {
      margin: 0.5rem 0;
      text-transform: capitalize;
    }
    .desc {
      opacity: 0.7;
      margin: 0.5rem 0;
      font-style: italic;
    }
    :global(img) {
      max-width: 100%;
    }
    :global(a) {
      color: var(--accent);
      text-decoration: none;
    }
    :global(pre) {
      background: var(--card-2);
      padding: 1rem;
      border-radius: 6px;
      overflow: auto;
    }
  }
</style>