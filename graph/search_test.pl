use strict;
use warnings;
use Graph::Search qw(node bfs dfs);
use 5.20.0;
use experimental qw(postderef);

my $root = node 'foo';
my $one = node 'bar';
my $two = node 'baz';
my $three = node 'quux';

push $root->{outgoing}->@*, $one;
push $root->{outgoing}->@*, $two;
push $one->{outgoing}->@*, $three;

push $three->{outgoing}->@*, $two;

my $foo = [];
dfs $root, $foo;
say "dfs";
say "----";
say $_->{id} for $foo->@*;

# just get the search order
my @search = bfs $root, sub {
    1;
};
say '';
say "bfs";
say "----";
say $_->{id} for @search;
