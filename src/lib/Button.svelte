<script lang="ts">
  import Icon from '$lib/Icon.svelte';

  export let to = '';
  export let action = () => {};
  export let target = '_self';
  export let icon: string | null = null;
  export let selected: boolean = false;

</script>

<svelte:element this={to ? 'a' : 'button'} href={to} on:click={action} {target} class:selected>
  {#if icon}<Icon name={icon} />{/if}
  <slot />
</svelte:element>


<style lang="scss">
  a, button {
    position: relative;
    color: var(--foreground);
    text-decoration: none;
    padding: 0.25rem 0.5rem;
    border-radius: 6px;
    transition: transform 200ms ease-in-out;
    overflow: hidden;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    border: 1px solid transparent;
    background: var(--card);
    cursor: pointer;

    &::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: var(--gradient);
      border-radius: 6px;
      z-index: -1;
      opacity: 0;
      transition: opacity 300ms ease-in-out;
    }

    &:hover, &.selected {
      transform: scale(1.05);
      &::before {
        opacity: 1;
      }
    }
  }
</style>