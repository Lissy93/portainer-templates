
<script lang="ts">
  import type { DockerHubResponse } from '$src/Types';
  import Icon from '$lib/Icon.svelte';

  export let info: DockerHubResponse;

  const formatBigNumber = (num: number): string => {
    if (!num) return '';
    const units = ['k', 'M', 'B'];
    let unitIndex = 0;
    let value = num;
    while (value >= 1000 && unitIndex < units.length) {
      value /= 1000;
      unitIndex++;
    }
    const decimalPlaces = num < 10000 || (num >= 100000 && num < 1000000) ? 0 : 1;
    return num < 1000 ? num.toString() : value.toFixed(decimalPlaces) + units[unitIndex - 1];
  };

  const formatDate = (dateTime: string): string => {
    if (!dateTime) return '';
    const date = new Date(dateTime);
    return new Intl.DateTimeFormat('en-US', {
      year: 'numeric',
      month: 'short',
      day: '2-digit',
    }).format(date);
  };

  const timeAgo = (dateTime: string): string => {
    if (!dateTime) return '';
    const elapsed = Date.now() - new Date(dateTime).getTime();
    const msPer = [60000, 3600000, 86400000, 2592000000, 31536000000];
    const units = ['minute', 'hour', 'day', 'month', 'year'];

    for (let i = 0; i < msPer.length; i++) {
      if (elapsed < msPer[i]) {
        const value = Math.floor(elapsed / (i > 0 ? msPer[i - 1] : 1));
        return value === 0 ? 'just now' : `${value} ${units[i - 1] || 'minute'}${value > 1 ? 's' : ''} ago`;
      }
    }
    return `${Math.floor(elapsed / msPer[4])} years ago`;
  };

  const makeRenderData = () => {
    const results = [
      { label: 'Pulls', value: formatBigNumber(info.pull_count), icon: 'download' },
      { label: 'Stars', value: formatBigNumber(info.star_count), icon: 'star' },
      { label: 'User', value: info.hub_user, icon: 'user' },
      { label: 'Created', value: formatDate(info.date_registered), icon: 'published' },
      { label: 'Updated', value: timeAgo(info.last_updated), icon: 'updated' },
      { label: 'Status', value: info.status_description, icon: 'status' }
    ];
    return results;
  };
</script>

<div class="stats">
  {#each makeRenderData() as stat}
    <div class="row">
      <span class="lbl">
        <Icon name={stat.icon} color="var(--accent)" />
        {stat.label}:
      </span>
      <span>{stat.value}</span>
    </div>
  {/each}
</div>

<style lang="scss">
  .stats {
    background: var(--card-2);
    padding: 1rem;
    border-radius: 6px;
    .lbl {
      font-weight: 500;
      margin-right: 0.5rem;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      :global(svg) { opacity: 0.7; }
    }
  }
</style>