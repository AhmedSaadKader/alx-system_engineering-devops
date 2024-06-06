# Fixes wrong extension in file `wp-settings.php`.

exec { 'fix-typo':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
