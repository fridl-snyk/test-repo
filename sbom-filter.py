import sys
import json

# Read the CycloneDX JSON document from stdin
sbom = json.load(sys.stdin)

# Get the component reference
component_ref = sbom['metadata']['component']['bom-ref']

# Find the dependencies that are directly related to the component
direct_dependencies = []
for dependency in sbom['dependencies']:
    if dependency['ref'] == component_ref:
        direct_dependencies.extend(dependency.get('dependsOn', []))

# Create a new dependencies item with direct dependencies
dependencies_item = {
    "ref": component_ref,
    "dependsOn": direct_dependencies
}

# Update the dependencies list with the new dependencies item
sbom['dependencies'] = [dependencies_item]

# Remove components that are not in the direct dependencies
component_refs = set(direct_dependencies + [component_ref])
sbom['components'] = [
    component for component in sbom['components']
    if component['bom-ref'] in component_refs
]

# Write the modified SBOM to stdout
json.dump(sbom, sys.stdout, indent=2)
