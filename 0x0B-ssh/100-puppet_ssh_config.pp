#  setting up my client SSH configuration file


exec {'config SSH client':
  command => "echo -e 'IdentityFile ~/.ssh/school\nPasswordAuthentication no\n' >> /etc/ssh/ssh_config",
  path    => '/bin:/usr/bin',
}
