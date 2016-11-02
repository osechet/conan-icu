from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(username="osechet", channel="stable")
    builder.add_common_builds(pure_c=False)
    filtered_builds = []
    for settings, options in builder.builds:
        if settings["arch"] == "x86_64":
            filtered_builds.append([settings, options])
    builder.builds = filtered_builds
    builder.run()
