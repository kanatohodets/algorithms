#!/usr/bin/env perl

use strict;
use warnings;
use 5.20.0;
use experimental qw(postderef signatures);
use Data::Dump qw(dump);

## no critic ProhibitSubroutinePrototypes

# fisher-yates, via Durstenfeld, via wikipedia
sub shuffle ($data, $start, $end) {
    for (my $i = $end - 1; $i >= $start; $i--) {
        my $j = int rand ($end - $start) + $start;
        $data->@[$j, $i] = $data->@[$i, $j];
    }
}

my @data = 0 .. 10;
shuffle \@data, 5, scalar @data;
say dump @data;
