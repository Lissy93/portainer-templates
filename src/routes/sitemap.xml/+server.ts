import type { RequestHandler } from '@sveltejs/kit';

import { templatesUrl, baseUrl } from '$src/constants';
import type { Template } from '$src/Types';

const fetchData = async () => {
  const data = await fetch(templatesUrl).then((res) => res.json());
  return await data.templates.map((d: Template) => `${baseUrl}/${d.title.toLowerCase().replace(/[^a-zA-Z ]/g, "").replaceAll(' ', '-')}`);
};

const generationDate = () => {
  const date = new Date();
  return `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}-${String(date.getDate()).padStart(2, '0')}`;
}

export async function GET() {
  const data = await fetchData();

  const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
  <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>${baseUrl}</loc>
    <lastmod>${generationDate()}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1</priority>
  </url>
    ${data.map((url: string) => `
      <url>
        <loc>${url}</loc>
        <lastmod>${generationDate()}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.8</priority>
      </url>`)
      .join('')}
  </urlset>`;

  return new Response(sitemap, {
    headers: { 'Content-Type': 'application/xml' }
    }
  );
}
