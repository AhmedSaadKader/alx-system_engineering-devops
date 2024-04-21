# Setting up SSH config file
include stdlib

file_line { 'SSH configuration':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  lines   => [
    '    PasswordAuthentication no',
    '    IdentityFile ~/.ssh/school',
  ],
  replace => true,
}
