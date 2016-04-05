#!/bin/bash
identify $1
convert $1 -define jpeg:extent=${2}kb $1
identify $1
