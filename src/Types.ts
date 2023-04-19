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
  image: string;
  restart_policy?: 'always' | 'unless-stopped' | 'on-failure' | 'no';
  ports?: string[];
  volumes?: Volume[];
  environment?: Environment[];
}

export interface Volume {
  bind: string;
  container: string;
}

export interface Environment {
  name: string;
  label?: string;
}
