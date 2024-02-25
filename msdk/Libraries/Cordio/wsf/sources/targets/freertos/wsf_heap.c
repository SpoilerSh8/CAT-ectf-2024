/*************************************************************************************************/
/*!
 *  \file   wsf_heap.c
 *
 *  \brief  Heap service.
 *
 *  Copyright (c) 2009-2018 Arm Ltd. All Rights Reserved.
 *
 *  Copyright (c) 2019-2020 Packetcraft, Inc.
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */
/*************************************************************************************************/

#include "wsf_types.h"
#include "wsf_assert.h"
#include "wsf_cs.h"
#include "wsf_trace.h"
#include "wsf_buf.h"
#include "wsf_math.h"
#include "wsf_os.h"
#include "FreeRTOS.h"

/**************************************************************************************************
  Macros
**************************************************************************************************/

#ifndef WSF_HEAP_SIZE
#if(PAL_CFG_LL_MAX == 1)
/* Larger link layer configurations will require more heap space. */
#define WSF_HEAP_SIZE       0x18000
#else
/* This is the minimum heap size. */
#define WSF_HEAP_SIZE       0x8000
#endif
#endif

/**************************************************************************************************
  Global Variables
**************************************************************************************************/

static void* freeStartAddr = 0;
static uint32_t freeLen = 0;

/*************************************************************************************************/
/*!
 *  \brief      Initialize the heap memory.
 */
/*************************************************************************************************/
static void wsfHeapInit(void)
{
    freeStartAddr = pvPortMalloc(WSF_HEAP_SIZE);
    freeLen = WSF_HEAP_SIZE;
}

/*************************************************************************************************/
/*!
 *  \brief      Reserve heap memory.
 *
 *  \param      size    Number of bytes of heap memory used.
 */
/*************************************************************************************************/
void WsfHeapAlloc(uint32_t size)
{
    /* Round up to nearest multiple of 4 for word alignment */
    size = (size + 3) & ~3;

    if(freeStartAddr == 0) {
        wsfHeapInit();
    }

    if(freeLen < size) {
        WSF_ASSERT(FALSE);
    }

    freeStartAddr += size;
    freeLen -= size;
}

/*************************************************************************************************/
/*!
 *  \brief      Get next available heap memory.
 *
 *  \return     Address of the start of heap memory.
 */
/*************************************************************************************************/
void *WsfHeapGetFreeStartAddress(void)
{
    if(freeStartAddr == 0) {
        wsfHeapInit();
    }

    return freeStartAddr;
}

/*************************************************************************************************/
/*!
 *  \brief      Get heap available.
 *
 *  \return     Number of bytes of heap memory available.
 */
/*************************************************************************************************/
uint32_t WsfHeapCountAvailable(void)
{
    if(freeStartAddr == 0) {
        wsfHeapInit();
    }

    return freeLen;
}

/*************************************************************************************************/
/*!
 *  \brief      Get heap used.
 *
 *  \return     Number of bytes of heap memory used.
 */
/*************************************************************************************************/
uint32_t WsfHeapCountUsed(void)
{
    if(freeStartAddr == 0) {
        wsfHeapInit();
    }

    return (WSF_HEAP_SIZE - freeLen);
}
