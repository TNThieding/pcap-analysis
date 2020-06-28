import os

from pcap_analysis import PacketAnalyzer


def main():
    output_lines = [
        "#############",
        "API Reference",
        "#############",
        "",
        ".. contents::",
        "   :local:",
        "",
        ".. automodule:: pcap_analysis",
        "",
        "*******",
        "Classes",
        "*******",
        "",
        "PacketAnalyzer",
        "==============",
        "",
        ".. autoclass:: pcap_analysis.PacketAnalyzer",
        "",
    ]

    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    arbitrary_pcap_file = os.path.join(repo_root, "tests", "arp.pcapng")
    packet_analyzer_ins = PacketAnalyzer(arbitrary_pcap_file)
    for analyzer in packet_analyzer_ins._analyzers:
        output_lines += [
            "    .. py:attribute:: " + analyzer.__class__.__name__.lower(),
            "",
            " " * 8 + analyzer.__doc__[:-1] + " accessor.",
            "",
        ]

    output_lines += [
        "*********",
        "Analyzers",
        "*********",
        "",
        "Access analyzer class instances through the ``PacketAnalyzer`` class. They",
        "should not be instantiated directly and used standalone!",
        "",
    ]

    for analyzer in packet_analyzer_ins._analyzers:
        output_lines += [
            analyzer.__class__.__name__.upper(),
            "=" * len(analyzer.__class__.__name__),
            "",
            ".. autoclass:: " + analyzer.__module__ + "." + analyzer.__class__.__name__,
            "   :members:",
            ""
        ]

    with open("api_reference.rst", "w") as fd:
        fd.write("\n".join(output_lines))


if __name__ == "__main__":
    main()
