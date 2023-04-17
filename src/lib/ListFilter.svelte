<script lang="ts">
  export let searchTerm: string;
</script>

<div class="title-row">
  <h2>Template List</h2>
  <div class="filters">
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
}
</style>