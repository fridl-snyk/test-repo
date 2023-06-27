This Python script can be used in conjunction with the Snyk Sbom [CLI tool](https://docs.snyk.io/snyk-cli/commands/sbom) or [API call](https://docs.snyk.io/snyk-api-info/get-a-projects-sbom-document-endpoint) to filter out all transitive dependencies from the generated CycloneDX JSON output.  The following command is one example of how to use the script to filter out the generated results.

```snyk sbom --format=cyclonedx1.4+json | python3 sbom-filter.py > filteredSBOM.json```
