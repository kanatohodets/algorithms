#!/usr/bin/env perl

use strict;
use warnings;
use 5.20.0;
use experimental qw(postderef signatures);
## no critic ProhibitSubroutinePrototypes

sub node ($id, $data) {
    return {
        id => $id,
        word => $data,
        outgoing => []
    };
}

# preorder
sub dfs ($node, $discovered) {
    push $discovered->@*, $node;
    foreach my $neighbor ($node->{outgoing}->@*) {
        dfs($neighbor, $discovered) if !grep { 
            $_->{id} == $neighbor->{id}
        } $discovered->@*;
    }
}

sub bfs ($root, $is_interesting) {
    my @discovered = ($root);
    my %explored = (
        $root->{id} => 1
    );

    my @interesting;
    while (@discovered) {
        my $current = shift @discovered;
        push @interesting, $current if $is_interesting->($current);
        foreach my $neighbor ($current->{outgoing}->@*) {
            if (not $explored{$neighbor->{id}}) {
                push @discovered, $neighbor;
                $explored{$neighbor->{id}} = 1;
            }
        }
    }
    return @interesting;
}

my $root = node 0, 'foo';
my $one = node 1, 'bar';
my $two = node 2, 'baz';
my $three = node 3, 'quux';

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
