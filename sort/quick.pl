#!/usr/bin/env perl
# in-place quicksort
use strict;
use warnings;
use 5.20.0;
use experimental qw(postderef signatures);
use Data::Dump qw(dump);
use List::Util qw(shuffle);

## no critic ProhibitSubroutinePrototypes

my $compare = 0;
my $swaps = 0;
sub partition ($data, $left, $right) {
    # pivot in the middle.
    my $pivot = int ($right + $left) / 2;
    my $pivotVal = $data->[$pivot];
    my $store = $left;

    $swaps++;
    $data->@[$pivot, $right] = $data->@[$right, $pivot];

    foreach my $i ($left .. $right - 1) {
        if ($data->[$i] <= $pivotVal) {
            $compare++;
            $swaps++;
            $data->@[$i, $store] = $data->@[$store, $i];
            $store++;
        }
    }
    $swaps++;
    $data->@[$store, $right] = $data->@[$right, $store];
    return $store;
}

sub quicksort($data, $start, $end) {
    if ($start < $end) {
        my $partition = partition($data, $start, $end);
        quicksort($data, $start, $partition - 1);
        quicksort($data, $partition + 1, $end);
    }
}

#my @data = (4, 0, 0, 3, 99, 1);
#my @data = shuffle (0 .. 10);
#my @data = (0, 0, 0, 0, 1, 0, 1, 0, 0, 1);
#
# O(n**2) if the pivot is the first item in the list
my @data =  (1, split '', 0 x 9);
my @orig = @data;

quicksort(\@data, 0, scalar @data - 1);
say dump @data;
say "$compare comparisons and $swaps swaps in data of len " . scalar @data . " data: ", dump @orig;
