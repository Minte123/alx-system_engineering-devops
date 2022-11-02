# A puppet module to fix the bug in wp-setting
exec { 'fix-phpp':
    provider => shell,
    command  => " sudo sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
}
