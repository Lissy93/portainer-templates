<script lang="ts">
  import { slide } from 'svelte/transition';
  export let categories: string[];
  export let selectedCategories: string[];
  export let toggleCategory: (category: string) => void;
</script>

<div class="categories" transition:slide>
  {#each Object.keys(categories) as category}
    <span
      on:click={() => toggleCategory(category)}
      class:selected="{selectedCategories.includes(category)}"
      class="cat"
    >{category}</span>
  {/each}
</div>

<style lang="scss">
.categories {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  margin: 1rem auto;
  padding: 0 1rem;
  max-width: var(--max-width);
  .cat {
    border: 1px solid transparent;
    padding: 0 0.3rem;
    margin: 0.25rem;
    line-height: 2rem;
    border-radius: 6px;
    text-transform: capitalize;
    background: var(--card);
    transition: all 0.3s ease-in-out;
    cursor: pointer;
    font-size: 0.9rem;
    &:hover, &.selected {
      background: var(--gradient);
    }
  }
}
</style>