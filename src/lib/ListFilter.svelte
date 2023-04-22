<script lang="ts">
  export let searchTerm: string;
  export let isCategoriesVisible: boolean;
  export let toggleCategories: () => void;
</script>

<div class="title-row">
  <h2>Template List</h2>
  <div class="filters">
    <button on:click={toggleCategories}>
      {isCategoriesVisible ? '▲' : '▼'} Categories
    </button>
    <input type="text" placeholder="Search..." bind:value={searchTerm} />
  </div>
</div>

<style lang="scss">
.title-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 1rem auto;
  padding: 0 1rem;
  max-width: var(--max-width);
  flex-wrap: wrap;
  h2 {
    font-size: 2rem;
    margin: 0;
  }
  .filters {
    input {
      background: var(--card);
      border: 1px solid transparent;
      color: var(--foreground);
      padding: 0.5rem 0.75rem;
      border-radius: 6px;
      transition:all 0.3s ease-in-out;
      &:focus, &:hover {
        box-shadow: var(--shadow);
      }
    }
  }
  button {
    color: var(--foreground);
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