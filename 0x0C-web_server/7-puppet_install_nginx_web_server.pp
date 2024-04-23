# Add stable version of nginx repository
exec { 'add nginx stable repo':
  command => 'sudo add-apt-repository ppa:nginx/stable',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# Update software packages list
exec { 'update packages':
  command => 'apt-get update',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  refreshonly => true,
}

# Install nginx
package { 'nginx':
  ensure     => 'installed',
  require    => Exec['update packages'],
}

# Allow HTTP
exec { 'allow HTTP':
  command => "ufw allow 'Nginx HTTP'",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  unless  => 'dpkg -l nginx | grep -q ^ii',
  require => Package['nginx'],
}

# Change folder rights
file { '/var/www/html':
  ensure => directory,
  mode   => '0755',
}

# Create index file
file { '/var/www/html/index.html':
  content => "Hello World!\n",
}

# Create 404 page
file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page\n",
}

# Nginx configuration
file { '/etc/nginx/sites-enabled/default':
  ensure  => file,
  content => template('nginx/default.conf.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
}

