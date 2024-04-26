.. SPDX-FileCopyrightText: 2021 Intel Corporation
..
.. SPDX-License-Identifier: CC-BY-4.0

===============================
 oneAPI Specification Releases
===============================


This document lists releases of oneAPI specifications.


oneAPI Specification
====================

Releases are listed below. See GitHub_ for the latest build.

.. _GitHub: https://github.com/uxlfoundation/oneapi-spec


1.3
---

.. list-table::
  :widths: 30 20 50
  :header-rows: 1

  * - Version
    - Date
    - View
  * - `1.3 rev 1`_
    - 2023-11-06
    - `HTML <versions/1.3-rev-1/>`__ `PDF <versions/1.3-rev-1/oneAPI-spec.pdf>`__
  * - `1.3 provisional rev 1`_
    - 2023-9-14
    - `HTML <versions/1.3-provisional-rev-1/>`__ `PDF <versions/1.3-provisional-rev-1/oneAPI-spec.pdf>`__

1.2
---

.. list-table::
  :widths: 30 20 50
  :header-rows: 1

  * - Version
    - Date
    - View
  * - `1.2 rev 1`_
    - 2022-11-10
    - `HTML <versions/1.2-rev-1/>`__ `PDF <versions/1.2-rev-1/oneAPI-spec.pdf>`__
  * - `1.2 provisional rev 1`_
    - 2022-9-8
    - `HTML <versions/1.2-provisional-rev-1/>`__ `PDF <versions/1.2-provisional-rev-1/oneAPI-spec.pdf>`__

1.1
---

.. list-table::
  :widths: 30 20 50
  :header-rows: 1

  * - Version
    - Date
    - View
  * - `1.1 rev 1`_
    - 2021-11-12
    - `HTML <versions/1.1-rev-1/>`__ `PDF <versions/1.1-rev-1/oneAPI-spec.pdf>`__
  * - `1.1 provisional rev 2`_
    - 2021-7-19
    - `HTML <versions/1.1-provisional-rev-2/>`__ `PDF <versions/1.1-provisional-rev-2/oneAPI-spec.pdf>`__
  * - `1.1 provisional rev 1`_
    - 2021-4-7
    - `HTML <versions/1.1-provisional-rev-1/>`__ `PDF <versions/1.1-provisional-rev-1/oneAPI-spec.pdf>`__


1.0
---

.. list-table::
  :widths: 30 20 50
  :header-rows: 1

  * - Version
    - Date
    - View
  * - `1.0 rev 2`_
    - 2020-10-21
    - `HTML <versions/1.0-rev-2/>`__ `PDF <versions/1.0-rev-2/oneAPI-spec.pdf>`__
  * - `1.0 rev 1`_
    - 2020-9-14
    - `HTML <versions/1.0-rev-1/>`__ `PDF <versions/1.0-rev-1/oneAPI-spec.pdf>`__

Release Notes
-------------

1.3 rev 1
~~~~~~~~~

Changes since 1.2

* oneDPL

  * Specified how random number generators and distributions support
    sycl::vec
  * Incremental improvements and fixes

* oneCCL

  * For oneCCL, we added new APIs for point to point send/recv
    operations.

* Level Zero

  See `Level Zero`_

* oneTBB

  * Allowed using pointers to class functions and members in place of
    function objects
  * Incremental improvements and fixes, including fixes in the oneTBB
    named requirements

1.3 provisional rev 1
~~~~~~~~~~~~~~~~~~~~~

1.2 rev 1
~~~~~~~~~

Changes since 1.1

* SYCL

  The following extensions were added:

  * `sycl_ext_oneapi_assert` - Support for device-side assert.
  * `sycl_ext_oneapi_default_context` - Adds the concept of a platform
    default context.
  * `sycl_ext_oneapi_discard_queue_events` - Adds a queue property
    that can optimize queues in some circumstances.
  * `sycl_ext_oneapi_srgb` - Exposes sRGB support for images.
  * `sycl_ext_oneapi_usm_device_read_only` - Adds a property for USM
    allocations.

* oneDPL

  The following updates were added in oneDPL specification for version 1.2:

  * The content was reorganized.
  * API for random number generation was added.
  * Incremental improvements and bug fixes.

* oneDNN

  This is a new major release of oneDNN spec, which breaks
  compatibility with previously published versions.

  * oneDNN Graph extension: a graph extension is added to allow
    seamless fusion of operations, and more flexibility for backend
    specific optimizations.
  * reworked quantization workflow: in order to support dynamic
    quantization efficiently and allow better reuse of primitive
    objects, quantization parameters are no longer passed at primitive
    creation, but at primitive execution.  This also allows to pass
    quantization parameters from device memory, instead of passing
    them from host memory.
  * opaque memory descriptors, and removal of operation descriptors:
    this allows more flexibility for oneDNN implementation to add new
    memory layouts and primitive extensions without breaking
    compatibility.
  * Better support for type conversion fusion: all primitives now take
    separate descriptors for input and output, which allows to fuse
    type conversions to all primitives.

* Level Zero

  See `Level Zero`_

* oneTBB

  The following updates were added in oneTBB specification for version
  1.2:

  * Support for core types and thread-per-core limit was added to
    task_arena constraints.
  * API of concurrent_queue and concurrent_bounded_queue was extended
    to better match C++ standard containers.
  * Incremental improvements and bug fixes.

* oneVPL

  This release updates oneVPL specification to version 2.9.0. New
  features include:

  * Deprecated mfxExtCodingOption2::BitrateLimit.
  * Added note that applications must call MFXVideoENCODE_Query() to
    check for support of mfxExtChromaLocInfo and mfxExtHEVCRegion
    extension buffers.
  * Added AV1 HDR metadata description and further clarified
    mfxExtMasteringDisplayColourVolume and
    mfxExtContentLightLevelInfo.
  * Added deprecation messages to the functions MFXQueryAdapters,
    MFXQueryAdaptersDecode, and MFXQueryAdaptersNumber.
    Applications should use the process described in oneVPL Dispatcher
    to enumerate and select adapters.
  * Fixed multiple spelling errors.
  * Added extension buffer mfxExtSyncSubmission to return submission
    synchronization sync point.
  * Added extension buffer mfxExtVPPPercEncPrefilte to control
    perceptual encoding prefilter.
  * Deprecated mfxPlatform::CodeName and corresponding enum values.
  * Added mfxExtendedDeviceId::RevisionID and extDeviceUUID to be
    aligned across multiple domains including compute and specify device
    UUID accordingly.
  * Added extension buffer mfxExtTuneEncodeQuality and correspondent
    enumeration to specify encoding tuning option.
  * Updated description of MFXEnumImplementations to clarify that the
    input mfxImplCapsDeliveryFormat determines the type of structure returned.
  * Updated mfxvideo++.h to use MFXLoad API.

* oneMKL

  The following updates were added in oneMKL specification for version
  1.2:

  * Dense matrix copy and transpose routines were added in the
    BLAS-like extensions
  * half/bfloat16 precision support were added to several L1 BLAS
    routines
  * The supported precisions for BLAS gemm and gemm_batch were updated
  * Several routines in BLAS had const attributes properly assigned to
    arguments
  * Add a missing constraint on parameter "n" for LAPACK orgqr
    routines
  * Improve directories tree of VM, RNG, Stats domains of oneMKL. Fix
    minor issues in RNG
  * Other changes include minor clarifications and bug fixes.


1.2 provisional rev 1
~~~~~~~~~~~~~~~~~~~~~

1.1 rev 1
~~~~~~~~~

Changes since 1.0

* Ray Tracing: Added

  * Ray tracing capabilities have been added to the oneAPI
    specification providing software developers across the industry
    the ability to “write once” for high-fidelity ray-traced
    computations across multiple vendors’ systems and
    accelerators. Standardizing these interfaces provides
    well-designed, tried and true APIs and options for a broad set of
    compute and rendering infrastructure development.

  * The ray tracing functionality is subdivided into several
    domains within the oneAPI Specification:

    * Geometric ray tracing computations
    * Volumetric computation and rendering
    * Image denoising
    * Scalable rendering and visualization infrastructure

  * The set of Ray Tracing APIs include the following, which
    are in active use via the Intel® oneAPI Rendering Toolkit:

    * Embree
    * Open Volume Kernel Library
    * Open Image Denoise
    * OSPRay

* oneMKL:

  Introduces additional batched APIs for dense linear algebra. Sparse
  matrix-dense matrix product has been extended to support both row
  and column major layout for the dense matrix. The input USM pointers
  in the vector math APIs are now const qualified. To align with
  changes in SYCL 2020, all oneMKL USM APIs were updated to take an
  (optional) std::vector of input events instead of
  sycl::vector_class. Other changes include minor clarifications and
  bug fixes.

* oneTBB:

  Introduces a way for collaborative one-time function processing
  (collaborative_call_once), mutex classes with adaptive waiting
  behavior (mutex, rw_mutex), the ability to wait for thread completion
  (task_scheduler_handle and the finalize function). Extended task_group
  and task_arena classes to support deferred task submission via
  the new task_handle class. Extended concurrent_hash_map with methods
  that support lookup for distinct key types.

* DPC++

  The new extensions listed as part of oneAPI 1.1 include simplified
  device selection through text-based filtering, a default context for
  each platform to simplify common coding patterns, interoperability
  with devices that use Level Zero as a backend, an easier to use
  kernel-scope local memory allocation mechanism, GPU-specific
  information queries, FPGA-specific performance tuning controls, and
  a sub-group mask feature.

  DPC++ features that were incorporated into the SYCL 2020 spec were
  removed from this document.

* oneVPL

  New AV1 encode features. Enabled support for planar I422, I210, and
  BGR formats. Added surface pool interface for surface management.

* Level Zero

  Updates included significantly improved image processing
  functionality, better interoperability with other APIs and operating
  systems, new extensions for floating-point atomics and additional
  subgroup operations, and extensions to tune and optimize the way
  memory is allocated and kernels are scheduled on specific devices.

1.1 provisional rev 2
~~~~~~~~~~~~~~~~~~~~~

* oneVPL: Updated to 2.4.0
* oneDAL: Updated some APIs
* oneMKL: bug fixes

1.1 provisional rev 1
~~~~~~~~~~~~~~~~~~~~~

* Ray Tracing: added to oneAPI specification
* VPL: Updated to 2.3.1
* Level Zero: Updated to 1.1.2
* oneDNN: Added graph API

1.0 rev 2
~~~~~~~~~

* Formatting fixes for PDF

1.0 rev 1
~~~~~~~~~

* Initial release

.. _`Level Zero`: https://spec.oneapi.io/releases/index.html#level-zero
