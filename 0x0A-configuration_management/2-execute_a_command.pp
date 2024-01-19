# Using Puppet, i'll be creating a manifest that kills a process named killmenow

exec {'pkill -f':
  command  => 'pkill killmenow',
}
