#!/usr/bin/env perl
use 5.20.0;
use strict;
use warnings;
use experimental 'postderef';
use experimental 'lexical_subs';

# it'd be nice to use a &@ prototype to get the
# pretty block syntax, but that prevents optionally leaving out
# the comparator function
sub not_builtin_sort {
    # lexical to close over the $cmp comparator function
    my sub merge_sort;
    my sub merge;

    # if the first thing is a coderef, assume it's for comparing
    # sorting an array of coderefs is left to 'sort'.
    # maybe a tad dense, just playing around.
    my $cmp = ref $_[0] eq 'CODE' ? shift : sub { shift() <= shift() };

    my @list = @_;

    return merge_sort(@list);

    sub merge {
        my @left = shift->@*;
        my @right = shift->@*;

        my @result;
        my $left_len = scalar @left;
        my $right_len = scalar @right;
        while ($left_len > 0 or $right_len > 0) {
            if ($left_len > 0 and $right_len > 0) {
                if ($cmp->($left[0], $right[0])) {
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

    sub merge_sort {
        my @list = @_;
        my $len = scalar @list;
        return @list if $len <= 1;

        my (@left, @right);
        my $middle = int $len / 2;

        push @left, $_ for @list[0 .. $middle - 1];
        push @right, $_ for @list[$middle .. $len - 1];

        @left = merge_sort(@left);
        @right = merge_sort(@right);

        merge(\@left, \@right);
    }
}

my @data = (4, 2, 1, 3);
say not_builtin_sort @data;
say not_builtin_sort sub { shift() >= shift() }, @data;
say not_builtin_sort sub { shift() ge shift() }, ('a' .. 'z');
