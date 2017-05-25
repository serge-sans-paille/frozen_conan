from conans import ConanFile, tools
import os


class FrozenConan(ConanFile):
    name = "frozen"
    version = "0.1"
    license = "Apache 2.0"
    url = "https://github.com/serge-sans-paille/frozen_conan"
    code_url = "https://github.com/serge-sans-paille/frozen"
    build_policy="always"
    # No settings/options are necessary, this is header only

    def source(self):
        '''retrieval of the source code here. Remember you can also put the code in the folder and
        use exports instead of retrieving it with this source() method
        '''
        self.run("git clone %s --depth=1" % self.code_url)

    def package(self):
        self.copy("*.h", dst="include", src="frozen/include")
