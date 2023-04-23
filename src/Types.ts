export interface PortainerAppTemplate {
  version: string;
  templates: Template[];
}

export interface Template {
  type: 1 | 2 | 3; // 1 = Container, 2 = Swarm stack, 3 = Compose stack
  title: string;
  description: string;
  categories: string[];
  platform: string;
  command?: string;
  interactive?: boolean;
  logo: string;
  image?: string;
  restart_policy?: 'always' | 'unless-stopped' | 'on-failure' | 'no';
  ports?: string[];
  volumes?: Volume[];
  env?: Environment[];
  repository?: {
    stackfile: string;
    url: string;
  };
}

export interface Volume {
  bind: string;
  container: string;
  readonly?: boolean;
}

export interface Environment {
  name: string;
  value?: string;
  label?: string;
  set?: string;
}

export interface Service {
  name: string;
  image?: string;
  entrypoint?: string;
  restart_policy?: 'always' | 'unless-stopped' | 'on-failure' | 'no';
  volumes?: Volume[];
  command?: string;
  ports?: string[];
  build?: string;
  interactive?: boolean;
  env?: Environment[];
  dockerStats?: DockerHubResponse;
}

export interface TemplateOrService extends Template, Service {}

export interface DockerHubResponse {
  user: string; // The user who owns the repository
  name: string; // The name of the repository
  namespace: string; // The namespace the repository belongs to
  repository_type: string; // The type of repository (e.g., 'image')
  status: number; // The status of the repository as a number
  status_description: 'active' | 'inactive'; // Description of the repository status
  description: string; // A brief description of the repository
  is_private: boolean; // Whether the repository is private or not
  is_automated: boolean; // Whether the repository is automated or not
  star_count: number; // The number of stars the repository has received
  pull_count: number; // The number of times the repository has been pulled
  last_updated: string; // The date and time the repository was last updated
  date_registered: string; // The date and time the repository was registered
  collaborator_count: number; // The number of collaborators on the repository
  affiliation?: string | null; // The affiliation of the user with the repo
  hub_user: string; // The user who created the repository on Docker Hub
  has_starred: boolean; // Whether the user has starred the repository or not
  full_description: string; // The full description of the repository
  permissions: {
    read: boolean; // Whether the user has read permissions on the repository
    write: boolean; // Whether the user has write permissions on the repository
    admin: boolean; // Whether the user has admin permissions on the repository
  };
  media_types: string[]; // An array of supported media types for the repository
  content_types: string[]; // An array of supported content types for the repository
}

export interface DockerCompose {
  version: string;
  services: {
    [serviceName: string]: {
      image: string;
      ports?: string[];
      environment?: { [envVar: string]: string };
      volumes?: string[];
      restart?: string;
      command?: string;
      build?: string | { context: string; dockerfile?: string };
      networks?: string[] | { [networkName: string]: { aliases?: string[] } };
      depends_on?: string[];
      labels?: { [labelName: string]: string };
    };
  };
  networks?: { [networkName: string]: {} };
  volumes?: { [volumeName: string]: {} };
}

