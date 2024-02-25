/******************************************************************************
 * Copyright (C) 2023 Maxim Integrated Products, Inc., All Rights Reserved.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a
 * copy of this software and associated documentation files (the "Software"),
 * to deal in the Software without restriction, including without limitation
 * the rights to use, copy, modify, merge, publish, distribute, sublicense,
 * and/or sell copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included
 * in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
 * OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
 * IN NO EVENT SHALL MAXIM INTEGRATED BE LIABLE FOR ANY CLAIM, DAMAGES
 * OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 * ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 * OTHER DEALINGS IN THE SOFTWARE.
 *
 * Except as contained in this notice, the name of Maxim Integrated
 * Products, Inc. shall not be used except as stated in the Maxim Integrated
 * Products, Inc. Branding Policy.
 *
 * The mere transfer of this software does not imply any licenses
 * of trade secrets, proprietary technology, copyrights, patents,
 * trademarks, maskwork rights, or any other form of intellectual
 * property whatsoever. Maxim Integrated Products, Inc. retains all
 * ownership rights.
 *
 ******************************************************************************/

#ifndef LIBRARIES_PERIPHDRIVERS_INCLUDE_MAX78000_MXC_H_
#define LIBRARIES_PERIPHDRIVERS_INCLUDE_MAX78000_MXC_H_

#ifdef __riscv
// TODO(JC): This is a somewhat ugly hack added to avoid
// implicit function warnings on RISC-V projects
// when LIB_BOARD was added to libs.mk.  When the
// RISC-V build system is improved to use libs.mk
// this should be removed.
#ifndef LIB_BOARD
#define LIB_BOARD
#endif
#endif

#include "mxc_device.h"
#include "mxc_delay.h"
#include "mxc_assert.h"
#include "mxc_errors.h"
#include "mxc_lock.h"
#include "mxc_pins.h"
#include "mxc_sys.h"
#include "nvic_table.h"
#ifdef LIB_BOARD
#include "board.h"
#endif

/*
 *  Peripheral Driver Includes
 */
#include "adc.h"
#include "aes.h"
#include "cameraif.h"
#include "crc.h"
#include "dma.h"
#include "flc.h"
#include "gpio.h"
#include "i2c.h"
#include "i2s.h"
#include "icc.h"
#include "lp.h"
#include "owm.h"
#include "pt.h"
#include "rtc.h"
#include "sema.h"
#include "spi.h"
#include "tmr.h"
#include "trng.h"
#include "uart.h"
#include "wdt.h"
#include "wut.h"

#endif // LIBRARIES_PERIPHDRIVERS_INCLUDE_MAX78000_MXC_H_
