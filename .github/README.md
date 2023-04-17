
<h1 align="center">Portainer Templates</h1>
<p align="center"><i>A compiled list of 400+ ready to go Portainer App templates</i></p>
<p align="center">
  <a href="https://portainer-templates.as93.net">
    🌐 <sup><b>portainer-templates.as93.net</b></sup><br>
    <img width="200" src="https://i.ibb.co/hMymwH0/portainer-templates-small.png" />
  </a>
</p>

> **TL;DR** Under Settings → App Templates in your Portainer GUI, paste this URL:<br>
> `https://raw.githubusercontent.com/Lissy93/portainer-templates/main/templates.json`<br>


## Intro

In Portainer, [App Templates](https://docs.portainer.io/user/docker/templates) enable you to easily deploy a container with a predetermined configuration, while allowing you to customize options through the web UI. Both single containers, and stacks are supported. While Portainer ships with some default templates (see [portainer/templates](https://github.com/portainer/templates)), it's often helpful to have 1-click access to many more apps, without having to constantly switch template sources.

This repo combines app templates from several [sources](#sources), to create a ready-to-go [template file](https://github.com/Lissy93/portainer-templates/blob/main/templates.json) containing all the apps you'll ever need.

---

## Usage

1. Log into your Portainer web UI
2. Under Settings --> App Templates, update the URL to
    - `https://raw.githubusercontent.com/Lissy93/portainer-templates/main/templates.json`
3. Now under Home --> App Templates, you should see all apps. Click one to deploy.

<details>
<summary>Show me...</summary>

<p align="center"><a href="https://portainer-templates.as93.net"><img width="800" src="https://i.ibb.co/XxGRjrs/portainer-templates-installation.gif" /></a></p>

</details>

Alternatively, when you start Portainer, you can append the `--templates` flag pointing to the templates URL. 

---

## Self-Hosting

```bash
git clone https://github.com/lissy93/portainer-templates.git portainer-templates
cd portainer-templates
docker build -t portainer-templates .
docker run -d -p "8080:80" portainer-templates
```

If you're running a fork of this repo, don't forget to replace [`lissy93`] with your own username.

Your templates file will then be served up, at: `http://docker-host:8080/templates.json`

Or, to mount the `templates.json` file to your container, so that you can make changes to it, and have them show up within Portainer

```bash
docker run -d -p "8080:80" -v "${PWD}/templates.json:/usr/share/nginx/html/templates.json" portainer-templates
```

---

## Editing

The `template.json` file is generated using the scripts in [`lib`](https://github.com/Lissy93/portainer-templates/tree/main/lib), using GitHub Actions.
Running the `make` command will download all listed sources, parse them, and combine them with anything in the sources dir, outputting the `templates.json` file.<br>
_So, you only need to edit **either** the [`sources.csv`](https://github.com/Lissy93/portainer-templates/blob/main/sources.csv) file, **or** add your templates directly into the [`sources/`](https://github.com/Lissy93/portainer-templates/tree/main/sources) directory._

### Adding a new Source
If you're maintaining your own list of Portainer templates, and would like them to be included, just add the URL to your template.json file to [`sources.csv`](https://github.com/Lissy93/portainer-templates/blob/main/sources.csv), along with a name.
When the action runs, it will download the content, parse it and add it to the final template.

### Adding a Template / Template list
Alternatively, place your template file within the [`sources`](https://github.com/Lissy93/portainer-templates/tree/main/sources) directory, and it will be automatically combined into the main `template.json`. Be sure that your template corresponds to [Portainer's App Template JSON Format](https://docs.portainer.io/advanced/app-templates/format).

### Validating Templates
There is a schema defined in [`Schema.json`](https://github.com/Lissy93/portainer-templates/blob/main/Schema.json), which can be used to validate any Portainer template.
Run `make validate` to ensure your template conforms to Portainer's App Template [specification](https://docs.portainer.io/advanced/app-templates/format).

### Maintaining your own Templates
If you'd like to use this repo as a base, but maintain your own list of template, just fork the repository, and update `lissy93` with your username in the import URL.

---

## Sources

Full credit to the authors of the following templates.
The main `templates.json` file is composes of these sources, along with the content of the [`sources`](https://github.com/Lissy93/portainer-templates/tree/main/sources) directory.

- [dnburgess](https://github.com/dnburgess/self-hosted-template) <sup>[`template.json`](https://raw.githubusercontent.com/dnburgess/self-hosted-template/master/template.json)</sup>
- [qballjos](https://github.com/Qballjos/portainer_templates) <sup>[`template.json`](https://raw.githubusercontent.com/Qballjos/portainer_templates/master/Template/template.json)</sup>
- [SelfhostedPro](https://github.com/SelfhostedPro/selfhosted_templates) <sup>[`template.json`](https://raw.githubusercontent.com/SelfhostedPro/selfhosted_templates/portainer-2.0/Template/template.json)</sup>
- [technorabilia](https://github.com/technorabilia/portainer-templates) <sup>[`template.json`](https://raw.githubusercontent.com/technorabilia/portainer-templates/main/lsio/templates/templates-2.0.json)</sup>
- [mikestraney](https://github.com/mikestraney/portainer-templates) <sup>[`template.json`](https://raw.githubusercontent.com/mikestraney/portainer-templates/master/templates.json)</sup>
- [xneo1](https://github.com/xneo1/portainer_templates) <sup>[`template.json`](https://raw.githubusercontent.com/xneo1/portainer_templates/master/Template/template.json)</sup>

---

## Supported Apps and Stacks

---

## Contributing

---

## Website
There's a simple website, which lists all available templates and shows the config options for each. You can view it at **[portainer-templates.netlify.app](https://portainer-templates.netlify.app/)**<br>
The source is located in the [`website`](https://github.com/Lissy93/portainer-templates/tree/website) branch, and it's build as a simple SSR Svelte app (using SvelteKit + TypeScript + SCSS + Vite).

To make changes to the website, you'll need Node.js and Git installed. Then just run the following commands:
```bash
git clone -b website git@github.com:Lissy93/portainer-templates.git # Clone the website branch
cd portainer-templates # Navigate into the directory
npm i # Install dependencies
npm run dev # Start the development server
```

And to pubish, run `npm run build` then either use `npm start` or host the content of the '/build' directory using a web server of your choice. Alternatively, there's a [Dockerfile](https://github.com/Lissy93/portainer-templates/blob/website/Dockerfile), for easy deployment :)

Note that it's not required to make any changes to the website when adding a new template or templates source, as data is fetched directly from [`templates.json`](https://github.com/Lissy93/portainer-templates/blob/main/templates.json) in the repo's main branch - so should show up automatically once your changes are merged.

---

## Disclaimer

---

## License



<!-- License + Copyright -->
<p  align="center">
  <i>© <a href="https://aliciasykes.com">Alicia Sykes</a> 2023</i><br>
  <i>Licensed under <a href="https://gist.github.com/Lissy93/143d2ee01ccc5c052a17">MIT</a></i><br>
  <a href="https://github.com/lissy93"><img src="https://i.ibb.co/4KtpYxb/octocat-clean-mini.png" /></a><br>
  <sup>Thanks for visiting :)</sup>
</p>

<!-- Dinosaur -->
<!-- 
                        . - ~ ~ ~ - .
      ..     _      .-~               ~-.
     //|     \ `..~                      `.
    || |      }  }              /       \  \
(\   \\ \~^..'                 |         }  \
 \`.-~  o      /       }       |        /    \
 (__          |       /        |       /      `.
  `- - ~ ~ -._|      /_ - ~ ~ ^|      /- _      `.
              |     /          |     /     ~-.     ~- _
              |_____|          |_____|         ~ - . _ _~_-_
-->

