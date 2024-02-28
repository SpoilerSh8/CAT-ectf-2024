/*
 * Copyright (C) 1999-2011, 2016 Free Software Foundation, Inc.
 * This file is part of the GNU LIBICONV Library.
 *
 * The GNU LIBICONV Library is free software; you can redistribute it
 * and/or modify it under the terms of the GNU Library General Public
 * License as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * The GNU LIBICONV Library is distributed in the hope that it will be
 * useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Library General Public License for more details.
 *
 * You should have received a copy of the GNU Library General Public
 * License along with the GNU LIBICONV Library; see the file COPYING.LIB.
 * If not, see <https://www.gnu.org/licenses/>.
 */

/*
 * CP50221 JISX0212 extensions
 */

static const unsigned short cp50221_0212_ext_2uni[112] = {
    /* 0x00 */
    0xfffd,
    0x2170,
    0x2171,
    0x2172,
    0x2173,
    0x2174,
    0x2175,
    0x2176,
    0x2177,
    0x2178,
    0x2179,
    0xfffd,
    0xfffd,
    0xfffd,
    0xfffd,
    0xfffd,
    /* 0x10 */
    0xfffd,
    0xfffd,
    0xfffd,
    0xfffd,
    0xfffd,
    0xff07,
    0xff02,
    0xfffd,
    0xfffd,
    0xfffd,
    0x70bb,
    0x4efc,
    0x50f4,
    0x51ec,
    0x5307,
    0x5324,
    /* 0x20 */
    0xfa0e,
    0x548a,
    0x5759,
    0xfa0f,
    0xfa10,
    0x589e,
    0x5bec,
    0x5cf5,
    0x5d53,
    0xfa11,
    0x5fb7,
    0x6085,
    0x6120,
    0x654e,
    0xfffd,
    0x6665,
    /* 0x30 */
    0xfa12,
    0xf929,
    0x6801,
    0xfa13,
    0xfa14,
    0x6a6b,
    0x6ae2,
    0x6df8,
    0x6df2,
    0x7028,
    0xfa15,
    0xfa16,
    0x7501,
    0x7682,
    0x769e,
    0xfa17,
    /* 0x40 */
    0x7930,
    0xfa18,
    0xfa19,
    0xfa1a,
    0xfa1b,
    0x7ae7,
    0xfa1c,
    0xfa1d,
    0x7da0,
    0x7dd6,
    0xfa1e,
    0x8362,
    0xfa1f,
    0x85b0,
    0xfa20,
    0xfa21,
    /* 0x50 */
    0x8807,
    0xfa22,
    0x8b7f,
    0x8cf4,
    0x8d76,
    0xfa23,
    0xfa24,
    0xfa25,
    0x90de,
    0xfa26,
    0x9115,
    0xfa27,
    0xfa28,
    0x9592,
    0xf9dc,
    0xfa29,
    /* 0x60 */
    0x973b,
    0xfffd,
    0x9751,
    0xfa2a,
    0xfa2b,
    0xfa2c,
    0x999e,
    0x9ad9,
    0x9b72,
    0xfa2d,
    0x9ed1,
    0xfffd,
    0xfffd,
    0xfffd,
    0xfffd,
    0xfffd,
};

static int cp50221_0212_ext_mbtowc(conv_t conv, ucs4_t *pwc, const unsigned char *s, size_t n)
{
    unsigned char c = *s;
    if (c < 0x70) {
        unsigned short wc = cp50221_0212_ext_2uni[c];
        if (wc != 0xfffd) {
            *pwc = (ucs4_t)wc;
            return 1;
        }
    } else if (c == 0xa1) {
        *pwc = 0x974d;
        return 1;
    }
    return RET_ILSEQ;
}

static const unsigned char cp50221_0212_ext_page21[16] = {
    0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, /* 0x70-0x77 */
    0x09, 0x0a, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, /* 0x78-0x7f */
};
static const unsigned char cp50221_0212_ext_page53[40] = {
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1e, /* 0x00-0x07 */
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, /* 0x08-0x0f */
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, /* 0x10-0x17 */
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, /* 0x18-0x1f */
    0x00, 0x00, 0x00, 0x00, 0x1f, 0x00, 0x00, 0x00, /* 0x20-0x27 */
};
static const unsigned char cp50221_0212_ext_page6d[16] = {
    0x00, 0x00, 0x38, 0x00, 0x00, 0x00, 0x00, 0x00, /* 0xf0-0xf7 */
    0x37, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, /* 0xf8-0xff */
};
static const unsigned char cp50221_0212_ext_page76[32] = {
    0x00, 0x00, 0x3d, 0x00, 0x00, 0x00, 0x00, 0x00, /* 0x80-0x87 */
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, /* 0x88-0x8f */
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, /* 0x90-0x97 */
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x3e, 0x00, /* 0x98-0x9f */
};
static const unsigned char cp50221_0212_ext_page7d[56] = {
    0x48, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, /* 0xa0-0xa7 */
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, /* 0xa8-0xaf */
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, /* 0xb0-0xb7 */
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, /* 0xb8-0xbf */
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, /* 0xc0-0xc7 */
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, /* 0xc8-0xcf */
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x49, 0x00, /* 0xd0-0xd7 */
};
static const unsigned char cp50221_0212_ext_page97[32] = {
    0x00, 0x00, 0x00, 0x60, 0x00, 0x00, 0x00, 0x00, /* 0x38-0x3f */
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, /* 0x40-0x47 */
    0x00, 0x00, 0x00, 0x00, 0x00, 0xa1, 0x00, 0x00, /* 0x48-0x4f */
    0x00, 0x62, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, /* 0x50-0x57 */
};
static const unsigned char cp50221_0212_ext_pagefa[40] = {
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x20, 0x23, /* 0x08-0x0f */
    0x24, 0x29, 0x30, 0x33, 0x34, 0x3a, 0x3b, 0x3f, /* 0x10-0x17 */
    0x41, 0x42, 0x43, 0x44, 0x46, 0x47, 0x4a, 0x4c, /* 0x18-0x1f */
    0x4e, 0x4f, 0x51, 0x55, 0x56, 0x57, 0x59, 0x5b, /* 0x20-0x27 */
    0x5c, 0x5f, 0x63, 0x64, 0x65, 0x69, 0x00, 0x00, /* 0x28-0x2f */
};
static const unsigned char cp50221_0212_ext_pageff[8] = {
    0x00, 0x00, 0x16, 0x00, 0x00, 0x00, 0x00, 0x15, /* 0x00-0x07 */
};

static int cp50221_0212_ext_wctomb(conv_t conv, unsigned char *r, ucs4_t wc, size_t n)
{
    unsigned char c = 0;
    if (wc >= 0x2170 && wc < 0x2180)
        c = cp50221_0212_ext_page21[wc - 0x2170];
    else if (wc == 0x4efc)
        c = 0x1b;
    else if (wc == 0x50f4)
        c = 0x1c;
    else if (wc == 0x51ec)
        c = 0x1d;
    else if (wc >= 0x5300 && wc < 0x5328)
        c = cp50221_0212_ext_page53[wc - 0x5300];
    else if (wc == 0x548a)
        c = 0x21;
    else if (wc == 0x5759)
        c = 0x22;
    else if (wc == 0x589e)
        c = 0x25;
    else if (wc == 0x5bec)
        c = 0x26;
    else if (wc == 0x5cf5)
        c = 0x27;
    else if (wc == 0x5d53)
        c = 0x28;
    else if (wc == 0x5fb7)
        c = 0x2a;
    else if (wc == 0x6085)
        c = 0x2b;
    else if (wc == 0x6120)
        c = 0x2c;
    else if (wc == 0x654e)
        c = 0x2d;
    else if (wc == 0x6665)
        c = 0x2f;
    else if (wc == 0x6801)
        c = 0x32;
    else if (wc == 0x6a6b)
        c = 0x35;
    else if (wc == 0x6ae2)
        c = 0x36;
    else if (wc >= 0x6df0 && wc < 0x6e00)
        c = cp50221_0212_ext_page6d[wc - 0x6df0];
    else if (wc == 0x7028)
        c = 0x39;
    else if (wc == 0x70bb)
        c = 0x1a;
    else if (wc == 0x7501)
        c = 0x3c;
    else if (wc >= 0x7680 && wc < 0x76a0)
        c = cp50221_0212_ext_page76[wc - 0x7680];
    else if (wc == 0x7930)
        c = 0x40;
    else if (wc == 0x7ae7)
        c = 0x45;
    else if (wc >= 0x7da0 && wc < 0x7dd8)
        c = cp50221_0212_ext_page7d[wc - 0x7da0];
    else if (wc == 0x8362)
        c = 0x4b;
    else if (wc == 0x85b0)
        c = 0x4d;
    else if (wc == 0x8807)
        c = 0x50;
    else if (wc == 0x8b7f)
        c = 0x52;
    else if (wc == 0x8cf4)
        c = 0x53;
    else if (wc == 0x8d76)
        c = 0x54;
    else if (wc == 0x90de)
        c = 0x58;
    else if (wc == 0x9115)
        c = 0x5a;
    else if (wc == 0x9592)
        c = 0x5d;
    else if (wc >= 0x9738 && wc < 0x9758)
        c = cp50221_0212_ext_page97[wc - 0x9738];
    else if (wc == 0x999e)
        c = 0x66;
    else if (wc == 0x9ad9)
        c = 0x67;
    else if (wc == 0x9b72)
        c = 0x68;
    else if (wc == 0x9ed1)
        c = 0x6a;
    else if (wc == 0xf929)
        c = 0x31;
    else if (wc == 0xf9dc)
        c = 0x5e;
    else if (wc >= 0xfa08 && wc < 0xfa30)
        c = cp50221_0212_ext_pagefa[wc - 0xfa08];
    else if (wc >= 0xff00 && wc < 0xff08)
        c = cp50221_0212_ext_pageff[wc - 0xff00];
    if (c != 0) {
        *r = c;
        return 1;
    }
    return RET_ILUNI;
}
