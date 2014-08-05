#!/usr/bin/env perl
use strict;
use warnings;
use 5.20.0;
use experimental 'postderef';

sub merge_sort {
    my @list = @_;
    my $len = scalar @list;
    say "merge_sort", @list;
    return @list if $len <= 1;

    my (@left, @right);
    my $middle = int $len / 2;

    push @left, $_ for @list[0 .. $middle - 1];
    push @right, $_ for @list[$middle .. $len - 1];
    say "left: ", @left;
    say "right: ", @right;

    @left = merge_sort(@left);
    @right = merge_sort(@right);

    merge(\@left, \@right);
}

sub merge {
    my @left = shift->@*;
    my @right = shift->@*;

    my @result;
    my $left_len = scalar @left;
    my $right_len = scalar @right;
    while ($left_len > 0 or $right_len > 0) {
        if ($left_len > 0 and $right_len > 0) {
            if ($left[0] <= $right[0]) {
                push @result, shift @left;
            } else {
                push @result, shift @right;
            }
        } elsif ($left_len > 0) { 
            push @result, shift @left;
        } elsif ($right_len > 0) {
            push @result, shift @right;
        }
        $left_len = scalar @left;
        $right_len = scalar @right;
    }

    @result;
}

my @data = (4, 3, 2, 1);
say merge_sort(@data);
