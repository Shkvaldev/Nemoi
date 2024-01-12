# Maintainer: DiLeT4nt

pkgname=nemoi-stt
pkgver=2.1.0
pkgrel=1
pkgdesc="Telegram bot for transcribing voice messages to text"
arch=("any")
url="https://github.com/Shkvaldev/Nemoi"
license=("GPL3")
depends=('python' 'python-pip' 'python-setuptools' 'ffmpeg' 'wget')
noextract=('srccode')
install=setup.install

package() {

    echo "[*] Creating pkg dir and placing files ..."
    mkdir -p ${pkgdir}/usr/share/nemoi-stt
	cp -r ../srccode ${pkgdir}/usr/share/nemoi-stt
    
    echo "[*] Placing systemd daemon config ..."
    mkdir -p ${pkgdir}/etc/systemd/system
    cp ../nemoi-stt.service ${pkgdir}/etc/systemd/system
}