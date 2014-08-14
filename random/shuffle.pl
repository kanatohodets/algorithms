#!/usr/bin/env perl

use strict;
use warnings;
use 5.20.0;
use experimental qw(postderef signatures);
use Data::Dump qw(dump);

## no critic ProhibitSubroutinePrototypes

# fisher-yates, via Durstenfeld, via wikipedia
sub shuffle ($data, $start, $end) {
    my @shuffled = $data->@*;
    for (my $i = $end - 1; $i >= $start; $i--) {
        my $j = int rand ($end - $start) + $start;
        @shuffled[$j, $i] = @shuffled[$i, $j];
    }
    return @shuffled;
}

my @data = 0 .. 10;
my @shuffled = shuffle \@data, 5, scalar @data;
say dump @shuffled;
