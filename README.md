### Goal

1. Absen sim kuliah secara otomatis

### Create file in secrets.json

File `secrets.json`

```json
{
  "username": "yourUsernameInSIMKULIAH",
  "password": "yourpasswordinSIMKULIAH"
}
```

### Logic

- [x] Buka halaman SimKuliah
- [x] Login dengan username(NIM) dan password
- [ ] Cek apakah ada absen atau tidak
- [ ] Konfirmasi kehadiran
- [ ] Exit app chrome driver

### future achievements

- [ ] Deploy on server
- [ ] set time for absent class

### Run Script

```buildoutcfg
python3 bot_sim.py
```
