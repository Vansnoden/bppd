'use server'

import { revalidatePath } from 'next/cache';
import { redirect } from 'next/navigation';
import { AuthError } from 'next-auth';
import { AUTH_URL } from './constants';
import { cookies } from 'next/headers'
import { signIn } from '../../auth.ts';
import { getDashboardData } from '@/services';
import { number } from 'zod';

export type State = {
    errors?: {
      status?: string[];
    };
    message?: string | null;
};

export async function authenticate(
  prevState: string | undefined,
  formData: FormData,
) {
  try {
    await signIn('credentials', formData);
  } catch (error) {
    if (error instanceof AuthError) {
      switch (error.type) {
        case 'CredentialsSignin':
          return 'Invalid credentials.';
        default:
          return 'Something went wrong.';
      }
    }
    throw error;
  }
}

export async function getToken(){
  const cookieStore = await cookies()
  const base_token = cookieStore.get('auth-token')
  const token = base_token?.value.split("__").join(" ")
  console.log("TOKEN: " + token)
  return token
}



