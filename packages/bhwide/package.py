# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

import os


class Bhwide(MakefilePackage):
    """BHWIDE is the state of art Monte Carlo for Bhabha generation at FCC-ee."""

    bhwide_version = "1.08"
    homepage = "https://placzek.web.cern.ch/bhwide/"
    url = f"https://github.com/ktht/bhwide/archive/refs/tags/{bhwide_version}.tar.gz"
    git = "https://github.com/ktht/bhwide.git" # unofficial copy

    tags = ["hep"]

    version(
        bhwide_version,
        sha256="10b34665c935208d1dad72a8c5698d3029212e1bd260b5e038fa6e7764a1b346",
    )

    patch(f"bhwide-{bhwide_version}-minimal.patch", level=0)

    depends_on("fortran", type="build")

    def build(self, spec, prefix):
        make()

    def install(self, spec, prefix):
        chmod = which("chmod")

        mkdirp(prefix.bin)

        install(join_path("bin", "bhwide"), join_path(prefix.bin, "BHWIDE.exe"))
        chmod("755", join_path(prefix.bin, "BHWIDE.exe"))

        script_sh = join_path(os.path.dirname(__file__), "BHWIDE")
        script = prefix.bin.BHWIDE
        install(script_sh, script)
        chmod("755", script)
