package workaround

// Copyright (c) Microsoft Corporation.
// Licensed under the Apache License 2.0.

import (
	"github.com/Azure/ARO-RP/pkg/util/version"
)

// Workaround is the interface for each Workaround
type Workaround interface {
	Name() string
	// IsRequired returns true when the clusterversion is indicates that the cluster
	// is effected by the bug that the workaround fixes.
	IsRequired(clusterVersion *version.Version) bool
	// Ensure will apply the workaround to the cluster.
	Ensure() error
	// Remove will remove the workaround from the cluster
	// (in the case when IsRequired returns false).
	Remove() error
}
