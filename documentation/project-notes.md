# Project Notes

## Purpose

The prototype demonstrates how an embedded controller can combine authentication, physical access control, feedback, logging and maintenance monitoring.

## Engineering Approach

**Input → Authentication → Decision → Physical Action → Feedback → Logging → Monitoring**

The binary-button input provides a low-cost way to demonstrate access-control logic that could later be connected to RFID/NFC hardware.

## Reliability

Main concerns identified during prototyping were input debouncing, temporary storage, breadboard wiring and network availability.

## Security

The binary codes in this repository are demonstration values and should not be used as real credentials. A production implementation should use stronger authentication, protected credentials, encryption, access-control policies and persistent audit storage.

## Project Context

This repository focuses on the technical prototype rather than assessment questions, marking criteria or university administration material.
