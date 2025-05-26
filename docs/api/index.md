# API Reference

Dokumentasi API ini dibuat secara otomatis untuk paket `generatecv`.

## Fungsi Inti

Fungsi utama untuk menghasilkan CV dan memuat data.

### `generatepdf()`
::: generatecv.pdf_generator.generatepdf

### `yamltocv()`
::: generatecv.pdf_generator.yamltocv

## Struktur Data Utama (`generatecv.models.CV`)

Model Pydantic utama yang menampung semua data CV.
::: generatecv.models.CV

### `PersonalInfo`
::: generatecv.models.PersonalInfo

### `Education`
::: generatecv.models.Education

### `CompanyExperience`
::: generatecv.models.CompanyExperience

### `Role`
::: generatecv.models.Role

### `Skill`
::: generatecv.models.Skill

### `Project`
::: generatecv.models.Project

### `Certificate`
::: generatecv.models.Certificate

### `Language`
::: generatecv.models.Language

### `Reference`
::: generatecv.models.Reference

## Modul Lainnya

### Styles
Modul `generatecv.styles` menangani penampilan visual dari PDF yang dihasilkan.

#### `BaseStyle`
::: generatecv.styles.base_style.BaseStyle

#### `ClassicStyle`
::: generatecv.styles.classic_style.ClassicStyle