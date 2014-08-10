#!/usr/bin/env perl

use strict;
use warnings;
use 5.16.3;

my $probe_count = 0;
sub bs {
    my ($list, $cmp, $key, $min, $max) = @_;
    return 'NOT FOUND' if $max < $min;
    my $mid = int (($max + $min) / 2) - 1;

    $probe_count++;
    my $mid_val = $list->[$mid];
    return $mid_val if $cmp->($key, $mid_val) == 0;
    return bs($list, $cmp, $key, $min, $mid + 1) if $cmp->($key, $mid_val) == -1;
    return bs($list, $cmp, $key, $mid + 1, $max);
}

my $max = rand() * 1_000_000;
my @a = (1 .. $max);
my $len = scalar @a;
my $cmp = sub { my ($a, $b) = @_; return $a <=> $b; };
say "found ", bs(\@a, $cmp, 9, 0, $len), " in ", $probe_count, " probes of list len ", $len;
say "expected at worst: ", (log $len) / (log 2), " probes";
