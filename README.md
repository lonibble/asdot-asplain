# asdot-asplain

python script to convert back and forth between asdot+ and asplain format

## Usage

```
Usage:
  ./asn-convert.py <asn>

    <asn> - ASN to convert in ASPLAIN or ASDOT+ format

Outputs ASPLAIN if given ASDOT+, and ASDOT+ if given ASPLAIN,
unless as 16-bit ASN, then no change
```

### Examples

Converts ASPLAIN to ASDOT+, ASDOT+ to ASPLAIN, and does nothing.

```
$ ./asn-convert.py 393523; ./asn-convert.py 6.307; ./asn-convert.py 65179
6.307
393523
65179
```

Converts ASPLAIN to ASDOT+, then back to ASPLAIN.

```
$ ./asn-convert.py `./asn-convert.py 393523`
393523
```

Converts ASDOT+ to ASPLAIN, then back to ASDOT+.

```
$ ./asn-convert.py `./asn-convert.py 6.307`
6.307
```

## Library use

makes 2 functions available:

*	`asdot2plain( asdot )`
*	`asplain2asdot( asplain )`

