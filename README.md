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

## Library use

makes 2 functions available:

*	`asdot2plain( asdot )`
*	`asplain2asdot( asplain )`

