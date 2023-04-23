<script lang="ts">
  import { slide } from 'svelte/transition';
  import Button from '$lib/Button.svelte';

  export let categories: string[];
  export let selectedCategories: string[];
  export let toggleCategory: (category: string) => void;

  const isSelected = (selected: string[], current: string) => selected.map((c) => c.toLocaleLowerCase()).includes(current.toLocaleLowerCase());
</script>

<div class="categories" transition:slide>
  {#each Object.keys(categories) as category}
    <Button
      action={() => toggleCategory(category)}
      selected="{isSelected(selectedCategories, category)}"
    >
    {category}
    </Button>
  {/each}
</div>

<style lang="scss">
.categories {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  margin: 1rem auto;
  padding: 0 1rem;
  gap: 0.25rem;
  max-width: var(--max-width);
}
</style>