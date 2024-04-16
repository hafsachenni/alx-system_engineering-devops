#fixing my nginx server to go from 943 failed http request to 0

exec {'replace':
    provider => shell,
    command  => 'sudo sed -i \'s/^ULIMIT=.*/ULIMIT="-n 4096"/g\' /etc/default/nginx',
    before   => Exec['restart'],
}

exec {'restart':
    provider => shell,
    command  => 'sudo service nginx restart',
}

exec
