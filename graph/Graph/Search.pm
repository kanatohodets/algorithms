package Graph::Search;
use strict;
use warnings;
use 5.20.0;
use experimental qw(postderef signatures);

use Exporter qw(import);
our @EXPORT_OK = qw(node dfs bfs);
## no critic ProhibitSubroutinePrototypes

my $id_counter = 0;
sub node ($data) {
    return {
        id => $id_counter++,
        word => $data,
        outgoing => []
    };
}

# preorder
sub dfs ($node, $discovered) {
    push $discovered->@*, $node;
    foreach my $neighbor ($node->{outgoing}->@*) {
        # a hash based set would be more efficient than grep,
        # but the results wouldn't be ordered.
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

1;
